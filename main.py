from services import replacement


if __name__ == '__main__':
    args = replacement.get_args()
    replacer = replacement.get_configuration(args.config)
    text_lines = replacement.get_text(args.text_file)
    text_lines = list(map(replacement.delete_line_break, text_lines))
    processed_text = replacement.processes_text(text_lines, list(replacer.keys()), list(replacer.values()))
    processed_text = replacement.invert_of_text(processed_text)
    replacement.write_file(args.text_file, processed_text)