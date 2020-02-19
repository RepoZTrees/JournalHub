# JournalHub

JournalHub is a static site generator application. It's a command-line tool which converts the contents of your blogs from markdown file format (filename.md), applies it to templates, and generates a purely static HTML files.

## Step by step instructions

1. `$ git clone https://github.com/RepoZTrees/JournalHub.git`
2. `$ cd JournalHub`
3. `$ pip install -r requirements.txt`
4. `$ python3 setup.py install`
5. Create an empty folder (for e.g. my_blogs). Create another folder inside **my_blogs** folder, and name it *blog_posts*. Put all your markdown (.md) files here
6. `$ journal init`
7. Copy *example.md* to a *new_filename.md*
8. Edit new_filename.md and save
9. `$ journal generate`
10. `$ journal serve`

## Command-line commands

- `$ journal -h`  **or**  `$ journal --help`
- `$ journal init`
- `$ journal generate`
- `$ journal serve`

## Authors

Shireen Sharaf,
Zuhara Sharin,
Roshna,
Majid KM,
Shahinshah Ummer,
Thenveer,
Vik Shah.

## Special Thanks

Noufal Ibrahim for his guidance and mentorship.


