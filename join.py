"""
Join temlate and script files into a single .vue file.
"""
import os
import re
import sys

def get_template_and_script_files(vue_file):
    # Read the content of the .vue file
    with open(vue_file, 'r') as vue_f:
        vue_content = vue_f.read()

    # Use regular expressions to extract src attributes
    template_match = re.search(r'<template src="([^"]+)"', vue_content)
    script_match = re.search(r'<script lang="ts" src="([^"]+)"', vue_content)

    if template_match and script_match:
        template_file = template_match.group(1)
        script_file = script_match.group(1)
        return template_file, script_file
    else:
        return None, None

def combine_vue_files(template_file, script_file, output_file):
    # Read the content of each file
    with open(template_file, 'r') as template_f, \
         open(script_file, 'r') as script_f:
        template_content = template_f.read()
        script_content = script_f.read()

    # Create the combined .vue file
    with open(output_file, 'w') as output_f:
        output_f.write('<template>\n')
        output_f.write(template_content)
        output_f.write('\n</template>\n')

        output_f.write('<script lang="ts">\n')
        output_f.write(script_content)
        output_f.write('\n</script>\n')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    vue_file = args.file
    template_file, script_file = get_template_and_script_files(vue_file)

    if template_file and script_file:
        output_file = "Combined_OCContentBox.vue"

        combine_vue_files(template_file, script_file, output_file)
        print(f"Combined .vue file created: {output_file}")
    else:
        print("Template and/or script file not found in the .vue file.")
