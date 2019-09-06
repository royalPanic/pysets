# PySets - v0.5

PySets is a combination of a couple of things. For one, it's a beginners project and my first published module. Secondly, it's a tool to help people who like me who are slightly annoyed at how similar yet different the concept of mathematical sets is to programming arrays (python lists).

## Some Notable Differences between **Sets** and **Arrays**.
### Writing:

Arrays come in one form, which is fairly universal.

`[1, 2, 3, 4, 5]`

Sets come in three forms. The first is **Semantic Description**, where the set is specified in writing.

`Set A is the set of integers greater than zero and less than six.`

The second form is known as **Roster Definition**. This is where the elements of the set are written out. (This form is closest to an array)

`Set A = {1, 2, 3, 4, 5}`

The last form is known as **Set-Builder Notation**. This is a more complex form used more often to present a set, and it can contains a **Semantic Description** inside it.

`Set A = {X | X is greater than zero and less than six. }`

### Elements:

There are some small differences in how the elements (or members) of a set are different than those of an array.

Namely, sets *begin counting at 1*, this is unlike arrays, in which the first element is element zero.

Also unlike arrays, sets *cannot contain duplicates*, all elements must be unique. The order the set is in also doesn't matter.
