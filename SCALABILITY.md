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


### How to scale it to 100 times ?

We have already optimized the code to reduce the latency. Now we need to scale the system to handle more requests at a single time. To accommodate more traffic we can use vertical scaling by increasing the available computational power, RAM, and bandwidth of the existing nodes of the system to make the system accommodate 10 times more requests than before. 10 times more traffic requests is easy to increase using vertical scaling. So once we are able to achieve that, the system now is in a position to handle 100 times more requests than the initial benchmarks. 

Initial benchmarks: 
Latency for 1 query = 27.881844 seconds
I.e, in 28 seconds 1 query is getting served
Code optimization:
After optimization of code latency for 1 query = 02.263997 seconds
That means in 28 seconds the system is able handle 10 times more requests
Vertical Scaling:
As we add more RAM to the system to make room for 10 times more requests, it means that in 28 seconds the system will handle 100 times more requests than the initial benchmark.
As there is a limitation to vertical scaling because of the hardware capabilities restriction, we can only scale till a certain point using vertical scaling.

