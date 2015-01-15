For today's miniquiz we will be finishing up our analysis of the ReadyChef data by calculating the Lifetime Value of a user.  We have already built many of the pieces and now we just need to put them together.


Define Cohorts by Campaign
=======================

Now we want to separate out the users by campaign type.

1. Create a view called cohort_by_campaign.  This will be a similar view as the first cohort we created yesterday (separated by campaign id this time though).

 | id | refr_source | month_acquired|
 |:----:|:-----------:|:----------------:|
 |   1 | PI          | 2013-04-01 00:00:00-07|
 |   2 | RE          | 2013-04-01 00:00:00-07|
 |   3 | RE          | 2013-04-01 00:00:00-07|
 |   4 | PI          | 2013-04-01 00:00:00-07|
 |   5 | RE          | 2013-04-01 00:00:00-07|
 | ...|...|...|

 Compare the cohorts retention rates by Campaign
 ================================

 Very similarly to what we did yesterday, calculate the retention rates by campaign cohort.  You will need to use the `months_visited` view from yesterday (if you didn't create a view for the user retention by month, feel free to use the code in the solution).

1. Create another view using the previous `months_visited` view and similar mechanics that we used yesterday to calculate the User cohort retention by month, but this time instead use the cohort by campaign view you just created in `1.`.

 | refr_source |      month_actual      | month_rank | uniques | fraction_retained|
 |:----------:|:---------------------:|:----------:|:-------:|:------------------|
 | FB          | 2013-04-01 00:00:00-07 |          1 |       1 |                 1|
 | FB          | 2013-05-01 00:00:00-07 |          2 |      19 |                19|
 | FB          | 2013-06-01 00:00:00-07 |          3 |      33 |                33|
 | FB          | 2013-07-01 00:00:00-07 |          4 |      39 |                39|
 | FB          | 2013-08-01 00:00:00-07 |          5 |      49 |                49|
 | FB          | 2013-09-01 00:00:00-07 |          6 |      53 |                53|
 | FB          | 2013-10-01 00:00:00-07 |          7 |      79 |                79|
 | FB          | 2013-11-01 00:00:00-07 |          8 |      88 |                88|
 | FB          | 2013-12-01 00:00:00-08 |          9 |     103 |               103|
 | FB          | 2014-01-01 00:00:00-08 |         10 |     115 |               115|
 | FB          | 2014-02-01 00:00:00-08 |         11 |      94 |                94|
 | FB          | 2014-03-01 00:00:00-08 |         12 |     191 |               191|
 | FB          | 2014-04-01 00:00:00-07 |         13 |     194 |               194|
 | PI          | 2013-04-01 00:00:00-07 |          1 |       2 |                 1|
 | PI          | 2013-05-01 00:00:00-07 |          2 |      23 |              11.5|
 | PI          | 2013-06-01 00:00:00-07 |          3 |      28 |                14|
 | ...|...|...|...|...|

 Lifetime Value
 ======================

 Life time value is defined as the average purchases of user per month. Do a cohort analysis on the users calculating the lifetime value on a monthly basis per cohort. There are a few ways to define LTV but for our sake here we will define it as: 

  > Total Money Spent per User per month X the life time of that user.

1. The table we want is simply the first half of this equation: each users total spend per month.  Using date_trunc on month, create a month by month purchase sum over the event type bought. This will require joining the Meal table as well (for the price).  This will then allow us to join this table with the cohort table to make the "life time" part of the "value" we just found.

 |  id  |         month          | total|
 |-----:|:---------------------:|:------|
 |    1 | 2013-04-01 00:00:00-07 |    82 |
 |    1 | 2013-05-01 00:00:00-07 |    24 |
 |    1 | 2013-06-01 00:00:00-07 |     7 |
 |    1 | 2013-07-01 00:00:00-07 |    14 |
 |    4 | 2013-05-01 00:00:00-07 |    37 |
 |    4 | 2014-02-01 00:00:00-08 |    12 |
 |    8 | 2013-05-01 00:00:00-07 |    13 |
 |   16 | 2013-04-01 00:00:00-07 |     7 |
 |   16 | 2013-05-01 00:00:00-07 |    11 |
 |   16 | 2013-07-01 00:00:00-07 |    10 |
 |   16 | 2013-09-01 00:00:00-07 |     7 |
 |...|...|...|