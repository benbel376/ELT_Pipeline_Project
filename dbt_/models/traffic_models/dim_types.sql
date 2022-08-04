{{ config(materialized='table') }}
with source_data as (
    select * from {{source("traffic_source_table", "source")}}
),

final as (
    SELECT distinct
    md5(types) as Id,
    types FROM source_data
)

select * from final