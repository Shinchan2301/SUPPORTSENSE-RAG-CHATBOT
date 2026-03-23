import pandas as pd
from pathlib import Path
import sys
print("Script started!", flush=True)

INPUT_FILE = "data/raw/sample_conversations.csv"
OUTPUT_FILE = "data/processed/cleaned_conversations.csv"

def clean_text(text):
    if pd.isna(text):
        return ""
    return " ".join(str(text).strip().split())

def main():
    try:
        print("Loading CSV file...", flush=True)
        df = pd.read_csv(INPUT_FILE)
        print("CSV loaded successfully!", flush=True)

        # Clean column names
        df.columns = [col.strip().replace("\n", " ").replace("  ", " ") for col in df.columns]

        # Rename important columns
        rename_map = {
            "Transcription": "text",
            "Notes": "notes",
            "Category": "category",
            "Intent": "intent",
            "Sentiment Category": "sentiment",
            "Sentiment Score": "sentiment_score",
            "User Risk Flag": "user_risk_flag",
            "Risk Type": "risk_type",
            "Intervention Triggered": "intervention_triggered",
            "Escalation Level": "escalation_level",
            "Block Required": "block_required",
            "Recovery Potential": "recovery_potential",
            "Chat Phase": "chat_phase",
            "Automation Confidence": "automation_confidence"
        }

        df = df.rename(columns=rename_map)

        # Keep useful columns only if they exist
        keep_cols = [
            "text",
            "notes",
            "category",
            "intent",
            "sentiment",
            "sentiment_score",
            "user_risk_flag",
            "risk_type",
            "intervention_triggered",
            "escalation_level",
            "block_required",
            "recovery_potential",
            "chat_phase",
            "automation_confidence"
        ]

        keep_cols = [col for col in keep_cols if col in df.columns]
        df = df[keep_cols].copy()

        # Clean text-like columns
        text_cols = [col for col in df.columns if df[col].dtype == "object"]
        for col in text_cols:
            df[col] = df[col].apply(clean_text)

        # Remove rows with empty main text
        df = df[df["text"].str.len() > 0].reset_index(drop=True)

        # Create processed folder if needed
        Path("data/processed").mkdir(parents=True, exist_ok=True)

        # Save cleaned file
        df.to_csv(OUTPUT_FILE, index=False)

        print("Preprocessing complete!", flush=True)
        print("Saved cleaned file to:", OUTPUT_FILE, flush=True)
        print("Shape:", df.shape, flush=True)
        print("\nColumns:", flush=True)
        print(df.columns.tolist(), flush=True)
        print("\nFirst 5 rows:", flush=True)
        print(df.head(), flush=True)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()