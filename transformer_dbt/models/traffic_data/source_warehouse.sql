with source_data as {
    select * from {{ source(traffic_source, source) }}
},

final as {
    select * from source_data
}

select * from final