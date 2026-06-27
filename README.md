## Task Overview
Utkrusht's assessment platform records detailed logs for online evaluations, including when candidates start tests, encounter errors, and complete their sessions. The operations and support teams currently rely on a simple script that only reports the total number of `ERROR` entries in a log file, which makes it hard to see which specific days experienced the most issues. You will extend this log analyzer to provide a daily breakdown of errors so the team can quickly spot problematic days and correlate them with deployments or infrastructure changes.

## Objectives
- Enhance the existing log analysis logic so it can compute how many `ERROR` entries occurred on each calendar day.
- Implement a new function that parses timestamps from log lines, identifies error-level entries, and aggregates counts per date using appropriate Python data structures.
- Ensure malformed or unexpected log lines do not crash the script by using structured error handling to skip invalid lines.
- Update the main script so that it prints both the existing total error count and a sorted, human-readable daily error report.
- Add at least one simple automated test that validates the daily error counting behavior for a known set of sample log lines.
- Keep the code readable, organized into functions and modules, and consistent with basic Python style conventions.

## How to Verify
- Run the main script and check that it still prints the overall number of `ERROR` lines as before based on the provided `logs.txt` data.
- Confirm that the script now also prints a daily breakdown, with one line per date in the format `YYYY-MM-DD: N errors`, sorted by date in ascending order.
- Verify that obviously malformed lines in the log file do not cause the program to terminate with a traceback, and that the rest of the valid lines are still processed.
- Introduce or adjust sample log data that includes errors on multiple days and confirm the counts match what you would expect if you inspected the file manually.
- Run your automated test(s) and check that they pass, demonstrating that your day-wise counting logic behaves correctly for the sample data.
- Quickly review your code to ensure function and variable names are clear, logic is not duplicated unnecessarily, and the implementation is easy to follow for another developer.

## Helpful Tips
- Consider how to isolate the responsibilities of reading the file, parsing individual log lines, and aggregating daily counts so that each function stays simple.
- Think about how to safely parse the timestamp portion of each line and what should happen if the format does not match what you expect.
- Explore using a dictionary or related standard library tools to accumulate counts keyed by date strings such as `YYYY-MM-DD`.
- Review how to sort dictionary keys so your final printed report is ordered by date rather than by insertion order or being unsorted.
- Consider writing a small set of representative example lines for your automated test instead of relying on the full `logs.txt` file.
- Think about how your error handling will make it clear that malformed lines are being skipped without stopping the entire analysis.