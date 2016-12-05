# stem-tagger
An app to tag stems, and map potential songs to relevant, searchable tags.
Currently moves files with certain keywords to different directories.

## Usage
``python organize.py [<settings-file>]``
Requires a file `settings.yml` (or the provided `<settings-file>` argument) that defines the following key-value pairs:
```yaml
patterns:
	DEFAULT_ALL:
	- <direct directory to tag mapping>

	<custom-tag>:
	-<list of destination folder>
include:
	- <list-of-extension>
```
