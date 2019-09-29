## Initial Ideas
* `Whitespace delimited word count` - regex split? what about punctuation?
* `line count` - split on new line. Don't forget windows line endings
* `# of letters per word` - functionality to count words. functionality to count letters. Divide
* `most common letter` - use letter count functionality

## Things to think about
* Handling large files
* Produce multiple stats per one read? If we run in parallel then multiple reads won't matter
* Binary files
* UTF-8

Other things: 

* Does most common letter include symbols?
* Restrict letter count to just alphabetical characters? Should it include numbers?
* Is `é` the same as `e` in most common letter?
* Refactor most common letter to letter count and inherit/compose it?
* Seperate test data from test by splitting into yaml files?

## Ideas
1) Library function which takes a string and returns a value

\- Disorganised  
\- Passing entire file contents as string could use lots of memory

2) Base reader class - extend to get functionality

\- Performs multiple reads, but maybe we could run in parallel.  
\- Better to use composition rather than inheritance - extension is not really a reader object!

3) Iterable

4) Read line by line - run plugin on each line

\+ One read.  
\- Over-complicating things?

Have a reader object or just pass file handle? Object helps with dependency inversion. With an Object for 2) we could add a lock on files at a later date. Will it be thread safe?

### Chosen Idea
4) Stats generator is given objects to run - command pattern

* each command:
  * `parse_line()`
  * `result()`

What if there are no lines e.g. one big line? Would use lots of memory. Could read by number of bytes but could end up only reading part of a word.

\- All plugins break if base interface changes!

## Extensiblity check
* Add average number of vowels per word
* Most common symbol

## Tests
* New line at end of file
* Binary file
* UTF-8
* Empty file

### Word count
* Number of words correct
* Mulitple `parse_line` runs
* Multiple white-space
* UTF-8
* Emtpy string

## Analysis
* Mixin or Composition for plugin tests?
  * Feel Composition might have been better than a Mixin for `base_stats_generator_test`, but not sure how it'd work with Python's unittest framework e.g. overloading the constructor could be fiddly
* RegexOccurances/RegexCount class which the others use to help with extensibility/flexibility e.g. it would give you a lot of control over what characters are counted. However, it is:
  * Slower
  * Increases coupling - if Regex class changes then classes using it can be affected
  * Violates YAGNI/KIS - can easily be added later if needed
* Making the definition of a letter configurable e.g. numerical characters improves flexibility for undefined requirements, but:
  * More code and testing which might not be needed thus adding unecessary complexity
  * Can easily add if needed
* Making letter equality configurable e.g. upper/lower case, accents
  * See point above
* Could use LetterOccurances when calculating LetterCount (e.g. sum the values in the dict)
  * Increases coupling
  * Slightly slower
