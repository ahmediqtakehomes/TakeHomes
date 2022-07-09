**Project:** 

Included in the email is a zip file of a subset of data pertaining to
users visiting the Gordon Ramsay MasterClass course marketing page for a
certain period of time. This data is captured by Segment's analytics.js
library and passed to Redshift, Amplitude, and other platforms. Please
find more context on the data provided below.

**Context:** This is data pulled from 11/1/2017 to 11/7/2017 of various
activity by individuals who had visited the Gordon Ramsay course
marketing page within the same period of time.

**Relevant Pages:** 

-   [[Homepage](https://www.masterclass.com/) ]{.underline}

-   [[Gordon Ramsay course marketing
    page]{.underline}](https://www.masterclass.com/classes/gordon-ramsay-teaches-cooking)
    (also known as a marketing landing page)

**Tables:** 

-   pages - major pageviews (homepage and course marketing page). 

-   homepage_click - any click on the homepage 

-   course_marketing_click - any click on the course marketing page
    (except purchase click) 

-   purchase_click - any \"take the class/give as a gift\" purchase on
    the course marketing page 

-   purchased_class - when a user purchases a class or an annual-pass.
    When a user purchases multiple items, there will be one row per item
    purchase.

These tables can give you a story of where the user went after they
landed and viewed one of our pages. Pages will give you an idea of where
they viewed, and then hompage_click and course_marketing_click are
clicks on those marketing pages. Then, once they begin the checkout
process with purchase_click, they finalize the process with
purchased_class.

**Fields** 

-   anonymous_id : an identifier given to unique device session 

-   received_at: when the event or page view occurred 

-   location: place on the page where the event occurred 

-   action: descriptor given to event 

-   channel_grouping: marketing bucket given to source of traffic ●
    paid: acquired via paid traffic 

-   organic-social-pr: free traffic via referrals, social networks, PR
    stories, etc. 

-   null: equivalent to organics 

-   traffic_source: origin of how the user came to the website ●
    ad_type: type of ad (e.g. video) 

-   acquisition_type: type of user that the marketing ad was intended
    towards 

-   prospecting: advertising to users who hadn't visited the website in
    at least 14 days 

-   remarketing: advertising to users who had visited the website in 14
    days ● lifecycle: advertising to users who have made a purchase
    and/or enrolled 

We are looking for this Data Analyst to be both reactive and proactive.
In this case, we want you to look at the data and pull insights about
the user behavior. When finished, please compile your response in
whatever format you consider most effective and email your output as
well as any code used to produce it.
