from redash_toolbelt.client import Redash

template = u"""/*
Name: {name}
Data source: {data_source}
Created By: {created_by}
Last Updated At: {last_updated_at}
*/
{query}"""


def save_queries(queries):
    for query in queries:
        filename = "/scripts/sql/query_{}.sql".format(query["id"])
        with open(filename, "w") as f:
            content = template.format(
                name=query["name"],
                data_source=query["data_source_id"],
                created_by=query["user"]["name"],
                last_updated_at=query["updated_at"],
                query=query["query"],
            )
            f.write(content)

def get_queries(**kwargs):
    redash_url = kwargs['redash_url']
    api_key = kwargs['api_key']

    redash = Redash(redash_url, api_key)
    queries = redash.paginate(redash.queries)
    save_queries(queries)