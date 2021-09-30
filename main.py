import argparse
import sys

from PyPDF2 import PdfFileMerger
import os


def merge_pdf(tmp_file: str, user_tmp_folder: str, output_dir: str) -> None:
    user_pdfs = os.listdir(user_tmp_folder)

    if len(user_pdfs) == 0:
        print("there is no files under {}, check path, exit".format(user_pdfs))
        exit(1)

    print("----Merging PDF Files----\n"
          "source_template: {}\n"
          "users_templates:{}\n"
          "output_path:{}\n".format(tmp_file, user_tmp_folder, output_dir))
    print("{} PDFs to merge".format(len(user_pdfs)))
    cnt = 1

    for f in user_pdfs:
        merger = PdfFileMerger(strict=False)
        merger.append(tmp_file)
        merger.append("{}/{}".format(user_tmp_folder, f))
        merger.write("{}/{}".format(output_dir, f))
        merger.close()
        print("{}/{} Merging PDF for {}".format(cnt, len(user_pdfs), f))
        cnt += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merging PDF tempalates.')

    parser.add_argument('--tmp-file', type=str,
                        help='full path of template file to be merged')
    parser.add_argument('--user-templates', type=str,
                        help='user template file folder')
    parser.add_argument('--output-dir', type=str,
                        help='folder to output merged PDf')

    args = args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    merge_pdf(args.tmp_file, args.user_templates, args.output_dir)