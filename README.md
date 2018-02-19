# This is a script I threw together a while ago that tries to calculate the
"real" date for Presidents' Day with some sort of circular average thing. For
extra fun, I also had it weight each president's contribution via total days in
office, net favorability rating, or a combination of both.

Sample output, as of 2018-02-19:
To get this result, append `45,Donald Trump,1946-06-14,"396",-14` to the CSV.

    Weighted (Days):         2000-02-28
    Weighted (Favorability): 2000-02-23
    Weighted (both):         2000-02-26
    Unweighted:              1999-12-05

Sample output, excluding Donald Trump (am too lazy to make the script auto
calculate days in office and all):

    Weighted (Days):         2000-02-25
    Weighted (Favorability): 2000-02-26
    Weighted (both):         2000-02-26
    Unweighted:              1999-12-07
