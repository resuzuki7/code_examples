# Problem

Given a string, identify the IP Addresses and Names.


## Example

- _input_: "Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe."
- _output_:
  - 127.0.0.1 and 123.4.5.6 are IP
  - Bob is a person


# Solution Provided

I used the _Spacy_ package to run basic Named Entity Recognition to identify People, and Regex to identify IP addresses.


## Pitfalls

### Oversimplication of NLP

This implementation uses a very simple application of Spacy.
I would closely monitor this process as it runs through several examples of the model.

I am assuming that other languages and specific names could be missed from the simple initial model. I would remedy this through re-training the model
the current set of data that the sample string came from, and validate with monitored examples of future problems.


### Not accounting for IPv6

In my methods, I am not considering IPv6s to be a valid IP address.
This can be remedied through the implementation of a more robust regex parameter that will account for these cases. 

### Blended information

If a user were to enter non-IP information in a format similar to an IP address, it could be wrongly classified as an IP address.
For example, a business in New York has the phone number: (212) 235-2668. If the person recording the initial string were to enter:
`Bob asked to be called back at 212.235.26.68.` the phone number could be interpreted as a valid IP.

### Foreign Proper Nouns

This implementation of _Spacy_ is trained on the English language.
It could have some problems identifying foreign names as people, even if they are recognized as entities. 

Additional training and languages could be added if necessary.

# Other methods considered

## Dictionary

In the scenario that this is problem is related to a support ticket system, the set of names that are relevant and being entered into the system will be limited.
For example, if the input string was changed to: "Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe. His cat, Catherine, meowed during the call.",
then both __Bob__ and __Catherine__ would be identified as names. A dictionary of the users' names or nicknames could be used to filter out irrelevant names,
or to identify the users as close matches.

This method would still involve NLP to tokenize the provided strings, and identify nouns to be compared to the dictionary.

## regex

Although [spacy is extremely fast](https://spacy.io/usage/facts-figures#speed-comparison) at performing its tasks,
if processing speed must be maximized, at the cost of accuracy, then we could attempt to use regex to identify names.

After splitting the string into tokens, a regex pattern could be used to identify potential names. This would be limited by
simple naming conventions (First letter capitalization, etc) and would output several false positives. 



## Next Steps

The following would be my recommendations for next steps:

- Validate performance on larger set of data
- Expand the implementation to larger models of spacy
- Expand IP Regex Recognition
  - Implement IPv6 validation
  - Include number verification within the regex pattern
