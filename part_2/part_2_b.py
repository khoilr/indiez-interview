from pyspark.sql import SparkSession
from pyspark.sql.functions import from_unixtime, min, udf
from pyspark.sql.types import StringType

print("======== Part 2 ========")

# * Read file
# Create a SparkSession
spark = SparkSession.builder.appName("Read Parquet File").getOrCreate()

# Read the parquet file
df = spark.read.parquet("./processing.parquet")

# Verbose
print("Schema and sample:")
df.printSchema()
df.show(5)


# * Extract project id
# Define a UDF to extract the project ID from the campaign name
@udf(returnType=StringType())
def extract_project_id(campaign_name):
    for campaign_name_split in campaign_name.split("_"):
        if len(campaign_name_split) >= 3 and campaign_name_split[:2].isupper() and campaign_name_split[2].islower():
            return campaign_name_split

    return None


# Add a new column 'project' by applying the UDF to the 'campaign_name' column
df = df.withColumn("project_id", extract_project_id(df["{campaign_name}"]))

# Verbose
print("Project unique IDs: ")
df_unique_project_id = df.select("project_id").distinct()
df_unique_project_id.show()


# * Find the earliest event time for each project
# Group the DataFrame by project_id and find the minimum event_time for each project
df_min_transaction_time = df.groupBy("project_id").agg(min(from_unixtime(df["{created_at}"])).alias("created_at"))

# Verbose
print("Project IDs and Earliest Event Time: ")
df_min_transaction_time.show()


# * Project ID sorted by number of campaign_name
# Get the count of each project_id
df_project_transaction_counts = (
    df.groupBy("project_id").count().withColumnRenamed("count", "transaction_count").orderBy("count", ascending=False)
)

# Verbose
print("Project IDs sorted by number of transactions descending: ")
df_project_transaction_counts.show()


# * Save the output to a parquet file and stop the SparkSession
# Write parquet file
df.write.parquet("./output.parquet", mode="overwrite")

# Stop the SparkSession
spark.stop()

print("======== Part 2 Done ========")
