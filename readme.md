# INDIEZ Interview

## Prerequisites

- Python3 (<https://www.python.org/downloads/>)
- pip (<https://pip.pypa.io/en/stable/installing/>)
- JDK 8 or higher (to run PySpark in part 2) (<https://www.oracle.com/java/technologies/javase-jdk11-downloads.html>)

## Instruction

### Part 1 - Programming

1. Navigate to the `part_1` directory
2. Install the required packages by running the following command: `pip install -r requirements.txt`. The `requirements.txt` only include the `tabulate` package which is used to display the results in a tabular format.
3. Run the following command: `python part_1.py`
4. The result will be logged to the console and saved to a csv file named `part_1.csv`

```bash
# From root directory
cd part_1
pip install -r requirements.txt
python part_1.py
```

The result should look like the following:

```bash
======== Part 1 ========
Sample ./test_1.csv
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|   {created_at} | {country}   | {os_name}   | {device_type}   | {random_user_id}                         | {store}   | {timezone}   | {network_type}   | {platform}   | {region}   | {time_to_reinstall}   | {time_to_uninstall}   |   {is_organic} | {hardware_name}   | {referral_time}   | {app_version}   | {time_spent}   | {label}   | {environment}   |
+================+=============+=============+=================+==========================================+===========+==============+==================+==============+============+=======================+=======================+================+===================+===================+=================+================+===========+=================+
|     1719842404 | ru          | android     | phone           | 4ffb687c0f07edb96cc2ad5d0fbb9013efa4814d | google    | UTC+0600     |                  |              |            |                       |                       |              0 |                   |                   | 2.3.1           |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842405 | ru          | ios         | phone           | f27d799c8b5d2427f4dc0c92b025dfed74edfdf0 | itunes    | UTC+0300     |                  |              |            |                       |                       |              0 |                   |                   | 240227296       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842405 | ro          | android     | phone           | 566f42e23314a9b43a54e902bd054a13bfd8d636 | google    | UTC+0300     |                  |              |            |                       |                       |              0 |                   |                   | 2.3.1           |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842407 | ru          | ios         | phone           | 04b696ff3a8a5fc10a16a21486d12606f81f7fcb | itunes    | UTC+0300     |                  |              |            |                       |                       |              0 |                   |                   | 240627199       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842408 | ru          | ios         | phone           | 0f0b91f63070ea2c14f969789f68d5344c7a4092 | itunes    | UTC+0300     |                  |              |            |                       |                       |              0 |                   |                   | 240627199       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
Sample ./test_2.csv
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
|   {created_at} | {country}   | {os_name}   | {random_user_id}                         | {timezone}   | {environment}   |   {is_organic} | {app_version}   | {platform}   | {region}   |
+================+=============+=============+==========================================+==============+=================+================+=================+==============+============+
|     1719842583 | tr          | ios         | 2eb22bda58da52abd8879eeb7ab1e2528c8ede32 | UTC+0300     | production      |              0 | 240627199       |              |            |
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
|     1719842545 | ru          | ios         | 6206fa6dca13fe731b39c41a0a474538142c7a5c | UTC+0300     | production      |              0 | 240627199       | mobile_app   |            |
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
|     1719842576 | by          | android     | abe59187a11648ddf5881d3755d2a41141f971da | UTC+0300     | production      |              0 | 2.3.1           |              |            |
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
|     1719842496 | ru          | android     | 6962d07fbc2cdfc7f649ca26b20d44725bf9f194 | UTC+0300     | production      |              0 | 2.3.1           |              |            |
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
|     1719842584 | ua          | android     | 848d2aef57a4f2d725b49608fe8a024e698c7045 | UTC+0300     | production      |              0 | 2.3.1           |              |            |
+----------------+-------------+-------------+------------------------------------------+--------------+-----------------+----------------+-----------------+--------------+------------+
Sample filled
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|   {created_at} | {country}   | {os_name}   | {device_type}   | {random_user_id}                         | {store}   | {timezone}   | {network_type}   | {platform}   | {region}   | {time_to_reinstall}   | {time_to_uninstall}   |   {is_organic} | {hardware_name}   | {referral_time}   | {app_version}   | {time_spent}   | {label}   | {environment}   |
+================+=============+=============+=================+==========================================+===========+==============+==================+==============+============+=======================+=======================+================+===================+===================+=================+================+===========+=================+
|     1719842404 | ru          | android     | phone           | 4ffb687c0f07edb96cc2ad5d0fbb9013efa4814d | google    | UTC+0600     |                  | Unknown      |            |                       |                       |              0 |                   |                   | 2.3.1           |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842405 | ru          | ios         | phone           | f27d799c8b5d2427f4dc0c92b025dfed74edfdf0 | itunes    | UTC+0300     |                  | Unknown      |            |                       |                       |              0 |                   |                   | 240227296       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842405 | ro          | android     | phone           | 566f42e23314a9b43a54e902bd054a13bfd8d636 | google    | UTC+0300     |                  | Unknown      |            |                       |                       |              0 |                   |                   | 2.3.1           |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842407 | ru          | ios         | phone           | 04b696ff3a8a5fc10a16a21486d12606f81f7fcb | itunes    | UTC+0300     |                  | Unknown      |            |                       |                       |              0 |                   |                   | 240627199       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
|     1719842408 | ru          | ios         | phone           | 0f0b91f63070ea2c14f969789f68d5344c7a4092 | itunes    | UTC+0300     |                  | Unknown      |            |                       |                       |              0 |                   |                   | 240627199       |                |           | production      |
+----------------+-------------+-------------+-----------------+------------------------------------------+-----------+--------------+------------------+--------------+------------+-----------------------+-----------------------+----------------+-------------------+-------------------+-----------------+----------------+-----------+-----------------+
======== Part 1 Done ========
```

### Part 2 - Data Processing

#### A. SQL

The SQL source code is in the file `part_2_a.sql`, and assume the table name is `tree` with filled data as

| id  | parent_id |
| --- | --------- |
| 1   | 4         |
| 2   | 4         |
| 3   | 7         |
| 4   | 5         |
| 5   | 7         |
| 6   | 5         |
| 7   | null      |
| 8   | 7         |
| 9   | 8         |
| 10  | 9         |
| 11  | 8         |
| 12  | 6         |
| 13  | 12        |
| 14  | 12        |
| 15  | 2         |

##### Define node type

```sql
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
```

| id  | parent_id | node_type |
| --- | --------- | --------- |
| 1   | 4         | leaf      |
| 2   | 4         | inner     |
| 3   | 7         | leaf      |
| 4   | 5         | inner     |
| 5   | 7         | inner     |
| 6   | 5         | inner     |
| 7   | null      | root      |
| 8   | 7         | inner     |
| 9   | 8         | inner     |
| 10  | 9         | leaf      |
| 11  | 8         | leaf      |
| 12  | 6         | inner     |
| 13  | 12        | leaf      |
| 14  | 12        | leaf      |
| 15  | 2         | leaf      |

##### List all descendants of a node

Breath First Search

```sql
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
```

The result will be

| id  | level | path         |
| --- | ----- | ------------ |
| 5   | 1     | 5            |
| 4   | 2     | 5->4         |
| 6   | 2     | 5->6         |
| 1   | 3     | 5->4->1      |
| 2   | 3     | 5->4->2      |
| 12  | 3     | 5->6->12     |
| 15  | 4     | 5->4->2->15  |
| 13  | 4     | 5->6->12->13 |
| 14  | 4     | 5->6->12->14 |

Depth First Search

```sql
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
```

The result will be

| id  | level | path         |
| --- | ----- | ------------ |
| 5   | 1     | 5            |
| 4   | 2     | 5->4         |
| 1   | 3     | 5->4->1      |
| 2   | 3     | 5->4->2      |
| 15  | 4     | 5->4->2->15  |
| 6   | 2     | 5->6         |
| 12  | 3     | 5->6->12     |
| 13  | 4     | 5->6->12->13 |
| 14  | 4     | 5->6->12->14 |

#### B. Data Processing using PySpark

1. Navigate to the `part_2` directory
2. Install the required packages by running the following command: `pip install -r requirements.txt`. This will install the `pyspark` package which is used to process the data.
3. Run the following command: `python part_2_b.py`
4. The result will be logged to the console and saved to a parquet file in the `output` directory

```bash
# From root directory
cd part_2
pip install -r requirements.txt
python part_2_b.py
```

The result should look like the following:

```bash
======== Part 2 ========
24/07/28 16:18:36 WARN Utils: Your hostname, Khoilr-MacBook-Air-M1.local resolves to a loopback address: 127.0.2.2; using 192.168.1.157 instead (on interface en0)
24/07/28 16:18:36 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/07/28 16:18:36 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Schema and sample:
root
 |-- {created_at}: string (nullable = true)
 |-- {campaign_name}: string (nullable = true)
 |-- {activity_kind}: string (nullable = true)
 |-- {country}: string (nullable = true)
 |-- {store}: string (nullable = true)

+------------+--------------------+---------------+---------+-------+
|{created_at}|     {campaign_name}|{activity_kind}|{country}|{store}|
+------------+--------------------+---------------+---------+-------+
|  1719842408|ss_min_NGi_Global...|     ad_revenue|       ru| itunes|
|  1719842412|ss_min_NGa_Global...|     ad_revenue|       ru| google|
|  1719842421|ss_min_NGa_Global...|     impression|       us| google|
|  1719842420|ss_min_NGa_Global...|     ad_revenue|       ru| google|
|  1719842422|ss_min_NGi_Global...|     ad_revenue|       ru| itunes|
+------------+--------------------+---------------+---------+-------+
only showing top 5 rows

Project unique IDs:
+----------+
|project_id|
+----------+
|       AZa|
|       KNi|
|       TRi|
| NGa-MiSto|
|       NGi|
|     TRiCN|
|       NGa|
|      NULL|
+----------+

Project IDs and Earliest Event Time:
+----------+-------------------+
|project_id|         created_at|
+----------+-------------------+
|      NULL|2024-06-03 03:51:55|
|       AZa|2024-05-14 16:09:04|
|       KNi|2024-04-09 21:21:16|
|       NGa|2024-05-06 12:15:41|
| NGa-MiSto|2024-07-01 20:27:16|
|       NGi|2024-05-04 20:08:45|
|       TRi|2024-04-27 16:34:21|
|     TRiCN|2024-02-12 19:39:18|
+----------+-------------------+

Project IDs sorted by number of transactions descending:
+----------+-----------------+
|project_id|transaction_count|
+----------+-----------------+
|     TRiCN|           104540|
|       NGa|            70497|
|       KNi|            33925|
|       TRi|            18535|
|       NGi|            14755|
|      NULL|              653|
|       AZa|              237|
| NGa-MiSto|                2|
+----------+-----------------+

======== Part 2 Done ========
```

## Run with Docker

> Only part 1 and 2-b are included in the docker-compose file, the part 2-a is sql file which is excluded.

### Prerequisites

- Docker (<https://docs.docker.com/get-docker/>)

### Instruction

Run `docker compose up` to start, the result of part 1 and 2 will be logged to the console respectively. The result of part 1 will be saved to a csv file named `part_1.csv` in `part_1` directory, and the result of part 2 will be saved to a parquet file in the `output` directory under `part_2` directory.
