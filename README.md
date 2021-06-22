# memo command
Its function is simple. Store memo to memos/key.txt and you can obtain memo by key or all.

## install
`pip install -U git+https://github.com/maruyu998/memo`

or 

```
git clone https://github.com/maruyu998/memo ~/.memo
pip install -e ~/.memo
```

## usage
```
> memo
[key1] 
memo1 memo1 memo1
[key2] 
memo2 momo2 memo2

> memo add key3
# vim is to be called when key3 is not exist

> memo vim key3
# vim is to be called

> memo rm key1
# key1 memo is to be removed

> memo ls
key1 key2 key3

> memo mv key1 test1
# memo that is named as key1 to be named as test1

> memo --help
usage: memo [-h] {get,add,vim,ls,rm,mv,push,pull} ...

positional arguments:
  {get,add,vim,ls,rm,mv,push,pull}

optional arguments:
  -h, --help            show this help message and exit
```