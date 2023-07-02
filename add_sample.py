from argparse import ArgumentParser, ArgumentError
from pathlib import Path
from shutil import copytree, rmtree

DEFAULT_PARENT_NAME = '~default~'
PROJECT_SAMPLES_PATH = Path('samples/')

def add_sample(sample_name, parent_name):
    sample_path: Path = PROJECT_SAMPLES_PATH / sample_name
    parent_path: Path = PROJECT_SAMPLES_PATH / parent_name

    if parent_name == DEFAULT_PARENT_NAME:
        sample_path.mkdir(parents=True)
        main_cpp: Path = sample_path / 'main.cpp'
        main_cpp.write_text('int main( int argc, const char **argv ) { return 0; }')
        return

    if sample_path.exists():
        raise FileExistsError('Sample already exists')

    if not parent_path.exists() and not parent_path.is_dir():
        raise FileNotFoundError('Parent sample folder does not exist')

    copytree(parent_path, sample_path, dirs_exist_ok=True)

def list_samples():
    for sample in PROJECT_SAMPLES_PATH.iterdir():
        if sample.is_dir():
            print(sample.name)

def remove_sample(sample_name):
    sample_path: Path = PROJECT_SAMPLES_PATH / sample_name

    if not sample_path.exists():
        raise FileNotFoundError('Sample does not exist')

    rmtree(sample_path)

def main():
    parser = ArgumentParser(prog='add_sample', description='Add sample to project')
    parser.add_argument('sample_name', help='new sample name', default='', nargs='?')
    parser.add_argument('-l', '--list', action='store_true', default=False, help='list all samples')
    parser.add_argument('-r', '--remove', action='store_true', default=False, help='remove sample')
    parser.add_argument('-p', '--parent', default=DEFAULT_PARENT_NAME, help='parent sample')
    args = parser.parse_args()

    if args.list:
        list_samples()
    elif args.remove:
        if args.sample_name == '':
            raise ArgumentError('No sample name provided')
        remove_sample(args.sample_name)
    else:
        if args.sample_name == '':
            raise ArgumentError('No sample name provided')
        add_sample(args.sample_name, args.parent)

if __name__ == '__main__':
    main()
