![Second Measure](logo.png)
# Applied Data Analyst | Short project (2-4 hours)

# Scope 

Use the data provided to answer the following questions:

1.  What is the market share between Grubhub and Doordash in the US?

2.  For members predominantly using DoorDash in January 2015, are they
    still predominantly using DoorDash or has their behavior changed?

# Deliverable 

Walk us through your approach and findings (\~20 minutes) during your
interview. Please be sure to include any assumptions you made. We're
flexible on the presentation format.

If you'd like, you may share your work (queries, scripts, and/or
results) with us ahead of or following your presentation.

# Sample 

The provided sample includes Grubhub and DoorDash transactions in the US
from 2014-01-01 to 2017-03-31.

The sample is delivered as a single gzipped, pipe-delimited file. You
can download the sample at the following link until July 30th at 6AM
(let us know if you need an extension):​

[[Click here to download the
data]{.underline}](https://secondmeasure-hiring.s3.amazonaws.com/candidate_short_project_grubhub_doordash/sample_000.gz?Signature=U2lW%2B1Ud4IaG%2FwNhjcf%2Bzjeim6I%3D&Expires=1565270524&AWSAccessKeyId=AKIAIU257ZBZ22KMV2EA)

  -------------------------------------------------------------------------
  **Column**    **Type**        **Description**
  ------------- --------------- -------------------------------------------
  company       STRING          Grubhub or DoorDash

  date          DATE            (ISO 8601) Date of transaction

  member_id     STRING          Unique member ID

  amount        DECIMAL(18,4)   Transaction amount (in USD)
  -------------------------------------------------------------------------

NOTE: Your evaluation is unrelated to any issues you might have
accessing the data and getting setup. Please reach out to us if you are
having issues.

Feel free to reach out to Matt Best (mbest@secondmeasure.com) with any
questions.
