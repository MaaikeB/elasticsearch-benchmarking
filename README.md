#  Search Benchmark

We want to be able to benchmark our search performance - to make sure that the things we are looking for appear in our
search results in the highest positions.

By having a fixed and stable measure we can test the performance of the search engine and monitor changes when data
changes or our code changes (sometimes both at the same time). Also we can test modifications to the search engine
configuration itself and see which configuration is best.

This works as follows:
For a project (for example OpenBudget) with an ElasticSearch DB we define certain searches and expected results can be
in a json configuration file.

For example:

```json
{
  "index_name": "corporations",
  "searches": [
    {
      "search": "red cows",
      "expected_results": ["Red Cow Corporation", "Rights for Red Cows"]
    }
  ]
}
```

Let's say at a given time the search is run in ElasticSearch and the results would be:
```json
{
  "results": [
    {"name": "Cows corporation red"},
    {"name": "Red Cow Corporation"},
    {"name": "Rights for Red Cows"},
    {"name": "Stam"},
    {"name": "Stam2"}
  ]
}
```

Since the expected results are on position 1 and 2, and there are a total of 5 resulst, the score would be 0.8
(For now a default scoring function is used, at a later stage the scoring function will be configurable)
This result is saved in the DB with the timestamp.

Let's say at a later time the search is run again, and now the results are on position 2 and 3, due to changes in the code.
The score will be 0.6, and this is also saved in the DB.

After a while we can look at these scores over time and get insights about the search performances.

## Development

### First phase

In the initial phase of the project, the program would perform the following functionality:
- Receives an input list of 'queries' and 'expected results'
- Performs searches according to the queries and tests, checks if the expected results appear and in which positions
- Gives a score (according to a default scoring function) for each query and a total score for the entire configuration

### Next phases

In future phases the following functionality will be added:
- Make the scoring function configurable
- A mechanism to run periodically (using cronjob)
- Saving the scoring results to DB
- Create a Web UI to view the results (in a graph and detailed results)

## Notes

#### Queries

Anything that can be fed to the search API (i.e. query, filters, sorting etc.)
We can separate the configuration and the 'query builder' mechanism, so that it's more modular and any 'query builder'
can be used (e.g. the BugetKey apies project query builder, but potentially also others) to create the ES query.

#### Expected results

Expected results can be specific document ids that should to return.
They can also be a predicate function returning True/False (e.g. for the query 'J. K. Rowling' on a library DB we expect
to see books that that she wrote, without specific preference for order).

#### Format

The input configuration can be provided in code, or in other form of configuration file.

### Scoring

The scoring function needs to be configurable - some would give a higher score to the first search page over the second,
others would prefer a more smooth scoring mechanism.

## Run the ElasticSearch Benchmarking tool

```buildoutcfg
python3 main.py --config_file_path='sample/config.json'
```


## Local development

In order to have an ElasticSearch server with data to run on, follow the below steps:
1. Install Dependencies:   
    a. Install Docker locally    
    b. Install Python dependencies:
    ```bash
    $ pip install dataflows datapackage-pipelines-elasticsearch
    ```
2. Go to the `sample/` directory
3. Start ElasticSearch locally:
   ```bash
   $ ./start_elasticsearch.sh
   ```

   This script will wait and poll the server until it's up and running.
   You can test it yourself by running:
   ```bash
   $ curl -s http://localhost:9200
    {
        "name" : "DTsRT6T",
        "cluster_name" : "elasticsearch",
        "cluster_uuid" : "QnLVHaOYTkmJZzkCG3Hong",
        "version" : {
            "number" : "5.5.2",
            "build_hash" : "b2f0c09",
            "build_date" : "2017-08-14T12:33:14.154Z",
            "build_snapshot" : false,
            "lucene_version" : "6.6.0"
        },
        "tagline" : "You Know, for Search"
    }
   ```
4. Load data into the database
   ```bash
   $ python load_fixtures.py
   ```

   You can test that data was loaded:
   ```bash
   $ curl -s http://localhost:9200/jobs/_count?pretty
    {
        "count" : 3516,
        "_shards" : {
                "total" : 5,
                "successful" : 5,
                "failed" : 0
        }
    }
   ```




