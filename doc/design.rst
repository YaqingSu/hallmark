Design
======

|hallmark|_ follows the
`Unix philosophy <https://en.wikipedia.org/wiki/Unix_philosophy#Origin>`_:

    Write programs that do one thing and do it well.
    Write programs to work together.
    Write programs to handle text streams, because that is a universal
    interface.

    -- Douglas McIlroy

The "one thing" for |hallmark|_ is maintaining a reproducible data
index.
With a well-designed indexing mechanism, it becomes natural to expose
a small set of core functions:

1.  **add/remove:**
    find data from any source and bring them into the index;

2.  **index:**
    compute checksums of data objects and index their relationships;

3.  **version control:**
    append immutable records; and

4.  **view:**
    emit manifests of subsets for other tools to consume.


|hallmark|_ Architecture
------------------------

A |hallmark|_ repository is the entry point for a version-controlled
dataset index.
It has three architecture components with different responsibilities:

1.  ``State``:
    the canonical in-memory data container, where all index mutations
    happen (add/remove/index);

2.  ``Dothm``:
    an on-disk version-controlled repository, persisting ``State`` and
    providing immutable history (using ``git``); and

3.  ``Worktree``:
    an on-disk working tree/directory, where data files are discovered
    and consumed.

The data flow can be summarized as::

    State ---persist-------+
      ^                    |
      |                    |
      |                    v
      +----instantiate-- Dothm (".hm" git repository)
      |                    ^
      |                    |link
      |                    v
      +-----discover---- Worktree
                           |
                           |access
                           v
                         Other tools


..  |hallmark| replace:: ``hallmark``

..  _hallmark: https://github.com/l6a/hallmark
