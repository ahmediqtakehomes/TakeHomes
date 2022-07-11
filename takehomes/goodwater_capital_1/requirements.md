![Goodwater Capital](logo.png)
# Commerce data exercise

Commerce is an age-old industry that has seen a lot of disruption over
the past couple of decades. From Amazon and eBay to more recent examples
like Stitch Fix and Dollar Shave Club, many companies have leveraged the
internet to create successful e-commerce businesses.

We hypothesize that these e-commerce "winners" exhibit similar patterns
or characteristics. If we can identify these patterns, we may be able to
use them to pick out future winners as well. To test this hypothesis, we
have collected sales data for several recent successful e-commerce
companies in `sales.csv`. 

Additionally, cohort-level data for several e-commerce companies are contained in the files:
```
blue_apron.csv
chewy.csv
dsc.csv
peloton.csv
ring.csv
stitch_fix.csv
warby_parker.csv
wish.csv
```

Using this data, please:

-   Propose a set of common patterns shared by these successful
    companies and formalize them as a precise rule that can be applied
    to other companies (a simple but useless example is "they all had at
    least \$1 of sales")

-   Interpret these patterns and evaluate whether they make intuitive
    sense in the context of e-commerce businesses and whether they would
    be useful for identifying future winners

[Brandless](https://brandless.com/) is an e-commerce company that sells
everyday essentials (e.g., snacks, tissues, soap) online. We also have
data on its sales in `brainless.csv`.

-   Using the full dataset, train a model that predicts future monthly
    sales and use this model to forecast Brandless's monthly sales over
    12 months (i.e., through September 2019)

-   Based on the data, the success patterns you identified, the
    forecasted sales, and any other information you think is relevant,
    how likely is Brandless to become a winner? Why?

-   What additional pieces of data/information would you want and what
    other analyses would you perform to make a higher conviction
    assessment?

Please prepare a presentation of your analysis that addresses the 5
questions above. Assume that the audience is data-savvy investors. Please
also include the code used to build the predictive model, preferably in
Python.

The following table describes what each column represents in the "Sales"
tab:

|Column|Description|
|---|---|
|`Company`|The Company Name|
|`Month`|The month that this row's data represents|
|`Sales`|Sales (revenue) generated during this month|
|`Customers`|# of customers who transacted during this month|
|`Transactions`|# of transactions during this month|

The other files contain cohort-based data for each of the companies:

|Column|Description|
|---|---|
|`Cohort month`|The month that this row's data represents
|`Cohort size`|# of customers who first transacted during this month|
|`1`|% of this cohort of customers who transacted again 1 month later|
|`2`|% of this cohort of customers who transacted again 2 month later
|...|...|
|`n`|% of this cohort of customers who transacted again $n$ month later|

For example: In January 2013, 25 customers transacted with Blue Apron
for the first time. In April 2013 (3 months later), 60% of these same
customers transacted with Blue Apron again.

Notes:

-   Sales, customers, and transactions are scaled down

-   New cohorts will have less data available because they have not had
    sufficient time to age
