#!/usr/bin/env python
import os
MEMOS_PATH = os.path.join(os.path.dirname(__file__),'memos')
if not os.path.exists(MEMOS_PATH): os.makedirs(MEMOS_PATH)
def _get_key_from_filename(path):
    return '.txt'.join(path.split('.txt')[:-1])
def _get_keys():
    return [_get_key_from_filename(filename) for filename in os.listdir(MEMOS_PATH)]
def _get_filepath_with_key(key):
    return os.path.join(MEMOS_PATH, f'{key}.txt')
def _exists_key(key):
    return os.path.exists(_get_filepath_with_key(key))
def _get_auto_increment_key():
    return str(max([0]+[int(key) for key in _get_keys() if key.isdecimal()])+1)
def _print_memo(key, maxline=50):
    with open(_get_filepath_with_key(key)) as f:
        for i, line in enumerate(f,1):
            print(line, end='')
            last = line[-1]
            if i>maxline:
                if last!='\n': print()
                print('...')
                break
def _call_vim(key):
    from subprocess import check_call
    check_call(['vim', _get_filepath_with_key(key)])

def show_all_memos(maxline=5):
    for key in _get_keys(): print(f'[{key}]'); _print_memo(key, maxline)

def show_memo(key):
    if not _exists_key(key): return
    _print_memo(key)

def add_memo(key):
    if _exists_key(key): print(f'key {key} already exists'); exit()
    _call_vim(key)

def edit_memo(key):
    _call_vim(key)

def ls_keys():
    print(*_get_keys(), sep='\t')

def rm_memo(key):
    if not _exists_key(key): return
    os.remove(_get_filepath_with_key(key))

def mv_memo_key(key_from, key_to):
    if not _exists_key(key_from): print(f'key {key_from} does not exist'); exit()
    if _exists_key(key_to): print(f'key {key_to} already exists.'); exit()
    os.rename(_get_filepath_with_key(key_from), _get_filepath_with_key(key_to))

def git_push():
    raise NotImplemented
def git_pull():
    raise NotImplemented

def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    get_parser = subparsers.add_parser('get')
    get_parser.add_argument('key')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('key')

    vim_parser = subparsers.add_parser('vim')
    vim_parser.add_argument('key')

    subparsers.add_parser('ls')
    
    rm_parser = subparsers.add_parser('rm')
    rm_parser.add_argument('key', nargs='+')

    mv_parser = subparsers.add_parser('mv')
    mv_parser.add_argument('key_from')
    mv_parser.add_argument('key_to')

    subparsers.add_parser('push')
    subparsers.add_parser('pull')

    args = parser.parse_args()

    if args.action == None:
        show_all_memos()
    
    elif args.action == 'get':
        show_memo(args.key)
    
    elif args.action == 'add':
        add_memo(args.key)

    elif args.action == 'vim':
        edit_memo(args.key)

    elif args.action == 'ls':
        ls_keys()

    elif args.action == 'rm':
        rm_memo(args.key)

    elif args.action == 'mv':
        mv_memo_key(args.key_from, args.key_to)

    elif args.action == 'push':
        git_push()

    elif args.action == 'pull':
        git_pull()

if __name__ == "__main__":
    main()