# Please ignore this file when build a release.
## How to build a release:
1. Priority of file:

|Function or method|Comment|
|:-----------------|:------|
|import modules    |Modules will be imported. Such like `import time`|
|Pre-variables out of `class vdir(object) :`|Such like `foo = 0`|
|`class vdir(object) :`| |
|Pre-variables in `class vdir(object) :`|Such like `foo = 0`|
|`def __init__(...) :`| |
|`def __str__(...) :`| |
|`def __repr__(...) :`| |
|other init functions|Such like `def __add__(...) :`|
|other functions   |Such like `def copy(...) :`|
|others           | |
