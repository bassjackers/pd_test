from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from src.models import Product, Purchase

# Create your views here.

def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    prod, _ = Product.objects.get_or_create(name=row[0])
                    Purchase.objects.create(
                        Product = prod,
                        price = int(row[2]),
                        quantity = int(row[1]),
                        date = row[3] + " " + row[5]
                    )


            obj.activated=True
            obj.save()
            success_message = "업로드 완료"
        except:
            error_message = "잘못된 방식"

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'csvs/upload.html', context)