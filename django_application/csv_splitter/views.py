from django.views.generic.base import TemplateView
from django.http import HttpResponse
import os
import csv


class CSVFileView(TemplateView):
    template_name = "csv_upload.html"

# Simple CSV Write Operation
def csv_simple_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'phone_number', 'country'])
    writer.writerow(['Huzaif', 'Sayyed', '+919954465169', 'India'])
    writer.writerow(['Adil', 'Shaikh', '+91545454169', 'India'])
    writer.writerow(['Ahtesham', 'Shah', '+917554554169', 'India'])

    return response



def split(filehandler, delimiter=',', row_limit=1000,
          output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)
