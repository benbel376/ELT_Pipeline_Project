{{ config(materialized='table') }}

with source_data as (
    select * from {{source("traffic_source_table", "source")}}
),

selection as (
    select track_id, md5(types) as type_id, traveled_d, avg_speed from source_data
),

dim_types as (
    select * from {{ref("dim_types")}}
), 

final as (
    select sel.track_id, dim_types.types, sel.traveled_d, sel.avg_speed
    from selection as sel 
    LEFT JOIN dim_types on sel.type_id = dim_types.Id
)

select * from final