Benchmarks & Scalability

### How we improved the application ?
To make our application scalable we have tried the first step to optimize the code to reduce latency. 

We tried to implement multi-threading which reduced the latency by 50 percent i.e, a single query that used to take 28 seconds came down to 14 seconds. 

Next we have optimized the way rest api is querying and limiting the number of results being parsed beyond the required number of results. 

These optimizations have lead to the query being 10 times faster than the initial benchmark.

| Improvement               | start time                 | end time                   | Time Taken    | Increase Factor |
|---------------------------|----------------------------|----------------------------|---------------|-----------------|
| Baseline                  | 2022-11-21 20:26:34.748957 | 2022-11-21 20:27:02.630801 | 0:00:27.881844 | x1              |
| Adding Multi Threading    | 2022-12-01 22:34:11.215863 | 2022-12-01 22:34:26.210865 | 0:00:14.995002 | x1.85           |
| Shifting HTML Parsers     | 2022-12-02 20:51:14.858636 | 2022-12-02 20:51:28.882232 | 0:00:14.023596 | x2              |
| Optimizing Scraping Logic | 2022-12-02 20:58:01.622125 | 2022-12-02 20:58:03.886122 | 0:00:02.263997 | x12.3           |

*All the above Experimental run results have been mentioned below for your reference. All the experiments were run on a macbook pro laptop with the same Internet Connection.

