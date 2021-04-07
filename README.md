# product-importer
Import products from a CSV file into database, with updates for existing records

## Specification
#### STORY 1: 
As a user, I should be able to upload a large CSV file of 500K products ( see here ) to the app. If there are existing
duplicates, it should overwrite the data. Deduplication can be done using the SKU of the product. SKU is case
insensitive. Though not in the CSV file, some products should be active and others should be inactive. The SKU is
expected to be unique.
#### STORY 2:
After I upload the file, I should be able to view all of the products, search and filter them. This is preferably on a URL
like /products . This view should also show a filter to see just the active products and inactive products.
#### STORY 3:
As a user, it should be possible to delete all existing records and start a fresh upload.

## Toolkit
1. Web framework: Python Django
2. ORM: Django ORM.
3. Database: postgres
4. Deployment: Heroku

## To Do

- [ ] file upload progress bar
- [ ] show import progress
- [ ] improved ui
- [ ] dynamic mapping of fields from csv file

## Improvements
1. Use `postgres copy` instead of `bulk_create`
2. Use `truncate` in place of `Model.objects.all().delete()`
3. Read CSV file in bathces instead of rows, and copy to database
4. Preprocess CSV to check for duplicates ad existing records

## WorkFlow
1. User uploads a CSV file
2. File is uploaded into an S3 bucket and the url is POSTed to view
3. The view calls the import_data function asynchronously
4. The import_data function loads the file from S3 into tmp/
5. Read file in chunks
6. For each row, an object for the Model is initialised and kept in a queue
7. On reaching chunk size, bulk_create is called
8. If bulk_create fails with 'Integrity Error' due to existing record, for each record in the chunk, update_or_create is called
