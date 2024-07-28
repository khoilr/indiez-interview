-- A
-- Assume table name is 'tree'
select
    id,
    parent_id,
    case
        when parent_id is null then 'root' -- Don't have parent_id -> root
        when id in ( -- Have at least one child -> inner
            select distinct
                parent_id
            from
                tree
        ) then 'inner'
        else 'leaf' -- Don't have child -> leaf
    end as node_type
from
    tree

-- B - Breath First Search
with
    bfs as (
        select
            1 as level,
            id,
            cast(id as varchar(255)) as path,
            parent_id
        from
            tree
        where
            id = 5
        UNION all
        select
            bfs.level + 1,
            t.id,
            bfs.path || '->' || t.id,
            t.parent_id
        from
            tree t
            inner join bfs on t.parent_id = bfs.id
    )
select
    id,
    level,
    path
from
    bfs

-- B - Depth First Search
with
    dfs as (
        select
            1 as level,
            id,
            cast(id as varchar(255)) as path,
            parent_id
        from
            tree
        where
            id = 5
        union all
        select
            dfs.level + 1,
            t.id,
            dfs.path || '->' || t.id,
            t.parent_id
        from
            tree t
            inner join dfs on t.parent_id = dfs.id
    )
select
    id,
    level,
    path
from
    dfs
order by
    path