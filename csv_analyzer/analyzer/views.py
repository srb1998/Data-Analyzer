from django.shortcuts import render
import pandas as pd
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UploadFileForm
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from io import BytesIO
matplotlib.use('Agg')
        
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                upload_file = request.FILES['file']
                data = pd.read_csv(upload_file)

                data['Order Date'] = pd.to_datetime(data['Order Date'])
                data = data.sort_values('Order Date')
                
                # Data Analysis
                head = data.head()
                summary_stats = data.describe().to_html()
                missing_values = data.isnull().sum().to_frame()
                
                # Data Visualization
                plot_images = []
                for column in ['Total Revenue', 'Units Sold', 'Total Profit']:
                    if column in data.columns:
                        img = BytesIO()
                        plt.figure()
                        sns.lineplot(x='Order Date', y=column, data=data)
                        plt.title(f'{column} over Time')
                        plt.xlabel('Order Date')
                        plt.ylabel(column)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.savefig(img, format='png')
                        plt.close()
                        img.seek(0)
                        plot_url = base64.b64encode(img.getvalue()).decode()
                        plot_images.append(plot_url)

                context = {
                    'form': form,
                    'head': head.to_html(),
                    'summary_stats': summary_stats,
                    'missing_values': missing_values.to_html(),
                    'plot_images': plot_images,
                }
                
                return render(request, 'result.html', context)
            except pd.errors.ParserError:
                return HttpResponse("The uploaded file is not a valid CSV.")
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        
        else:
            return HttpResponse("Invalid form submission.")
        
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
                
        