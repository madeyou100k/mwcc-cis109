# LAB 06: Bulk Text Transformer Utility

import argparse

# Convert text to uppercase.
def transform_upper(text):
    return text.upper()

# Convert text to lowercase.
def transform_lower(text):
    return text.lower()

# Count the number of words in the text.
def get_word_count(text):
    words = text.split()
    return len(words)

# Filter out strings that are too short.
def filter_short(text, min_length):

    if len(text) > min_length:
        return text
    else:
        return None
    
# Main program starts here.
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Bulk Text Transformer Utility"
    )

    # Allow the user to choose a transformation action.
    parser.add_argument(
        "--action",
        required=True,
        choices=["upper", "lower", "count", "filter"],
        help="Choose upper, lower, count, or filter"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Enter text separated by commas"
    )

    parser.add_argument(
        "--min_length",
        type=int,
        default=3,
        help="Minimum length used for filtering"
    )

    # Read the command-line arguments entered by the user.
    args = parser.parse_args()

    text_list = args.data.split(",")

    for text in text_list:

        text = text.strip()

        # Convert the text to uppercase.
        if args.action == "upper":
            result = transform_upper(text)

        # Convert the text to lowercase.
        elif args.action == "lower":
            result = transform_lower(text)

        # Count the words in the text.
        elif args.action == "count":
            result = get_word_count(text)

        # Filter strings based on their length.
        elif args.action == "filter":
            result = filter_short(text, args.min_length)

        # Print the result if it was not filtered out.
        if result is not None:
            print(result)
