Use Cases
=========

This section describes representative workflows supported by the
current |hallmark|_ CLI and Python API.


1. CLI: Standard Repository Ingest
----------------------------------

Alice is organizing telescope data in a normal directory.
She initializes that directory as a |hallmark|_ worktree::

    hallmark init obs
    cd obs

She adds the files using a python format-string pattern::

    hallmark add "{site}/{year:d}/{day:d}.fits"

She then commits the updated hallmark index::

    hallmark commit -m "Initial observation ingest"

She can inspect current repository paths at any time::

    hallmark info

She can also inspect current changes and commit history::

    hallmark status
    hallmark log

These git-like commands report or modify hallmark tracked state files
in ``.hm``.
Dataset files are represented through staged ``sha1`` column in
``data.tsv``, with other useful parameters (e.g., site, year, day),
associated with each file in different rows.


2. CLI: Bare Repository with Worktree Ingest
--------------------------------------------

Bob prefers managing a bare hallmark repository for storage and
staging data from a linked worktree.
He initialized the bare repository and verify its mode::

    hallmark init --bare sim.hm
    cd sim.hm
    hallmark info

He then attaches a worktree, stages discovered files, and commits::

    hallmark worktree add /data/outputs
    cd /data/outputs
    hallmark add "run{run:d}/frame{frame:d}.h5"
    hallmark status
    hallmark diff
    hallmark commit -m "Simulation snapshots"

The commit updates the same bare repository that owns the linked
worktree.


..  |hallmark| replace:: ``hallmark``

..  _hallmark: https://github.com/l6a/hallmark
