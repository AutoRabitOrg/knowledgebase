# Squash and Merge

### Introduction <a href="#introduction" id="introduction"></a>

Squashing lets you tidy up the commit history of a branch when accepting a merge request. It applies all of the changes in the merge request as a single commit, and then merges that commit using the merge method set for the project. The squashed commit’s default commit message is taken from the merge request title.

### When to Squash? <a href="#when-to-squash" id="when-to-squash"></a>

For instance, you may have worked on a project and generated plenty of commits for your reference. At some point, you will surely want to commit and consequently merge your work to the master branch. This is one instance when you need to squash all the commits into one so that all the previous as well the current commits are merged into one.

### What happens when you squash commits? <a href="#what-happens-when-you-squash-commits" id="what-happens-when-you-squash-commits"></a>

Squashing a commit means, from an idiomatic point of view, to move the changes introduced in said commit into its parent so that you end up with one commit instead of two (or more). If you repeat this process multiple times, you can reduce all commits to a single one.

Let’s assume you have the following commit log in the branch you want to merge as part of your merge request:

```
$ git log
commit d65ac9eaaa5a9f92cc2182ccd3cb6e930981842b (HEAD -> master, origin/master)
Author: dipender <dipender.s@autorabit.com>
Date:   Sun Feb 6 17:57:12 2022 +0530

    seventh commit

commit b6fa7c63c0a8563aff9b7b70f526003b7842e62f
Author: dipender <dipender.s@autorabit.com>
Date:   Sun Feb 6 17:56:54 2022 +0530

    sixth commit

commit ab176dfc5d096a51bc9e63effc280f348b714581
Author: dipender <dipender.s@autorabit.com>
Date:   Sun Feb 6 17:55:47 2022 +0530

    fifth commit

commit 64710907985cd4a2c331686d7fb0d24b9aabf2b0
Author: dipender <dipender.s@autorabit.com>
Date:   Sun Feb 6 14:34:35 2022 +0530

    bugfix branch

    4th commit
```

Here we want to squash the fifth, sixth, and seventh commit and create a new commit on top of commit 64710 (lets name it as target).

**After Squash:**

This results in a single commit with a commit message that is a concatenation of all three messages. All intermediary commits are gone and ready to merge!

```
$ git log
commit 315373283dcbe1c7561e93a32969fbab0943ad37 (HEAD -> master, origin/master)
Author: dipender <dipender.s@autorabit.com>
Date:   Sun Feb 6 17:55:47 2022 +0530

    fifth commit

    sixth commit

    seventh commit

commit 64710907985cd4a2c331686d7fb0d24b9aabf2b0
Author: dipender <dipender.s@autorabit.com>
Date:   Sun May 6 14:34:35 2022 +0530

    bugfix branch

    4th commit
```

### How to perform Squash and Merge for your merge request in the ARM tool <a href="#how-to-perform-squash-and-merge-for-your-merge-request-in-the-arm-tool" id="how-to-perform-squash-and-merge-for-your-merge-request-in-the-arm-tool"></a>

All you have to do is select the **Squash and Merge** checkbox while creating a merge request.

Explore: **Version Control > Merge Request History > New Merge Request**.

<figure><img src="../../../../../.gitbook/assets/image (79).png" alt="" width="563"><figcaption></figcaption></figure>

### When to delete source branch in squash merge? <a href="#when-to-delete-source-branch-in-squash-merge" id="when-to-delete-source-branch-in-squash-merge"></a>

Squash merging condenses the history of changes in your default branch, so it is important to work with your team to decide when you should squash merge and when you want to keep the full commit history of a topic branch. When squash merging, it’s a good practice to delete the source branch.
