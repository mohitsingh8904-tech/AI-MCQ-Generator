import io
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def render_to_pdf(template_path, context, filename="quiz_result.pdf"):
    html = render_to_string(template_path, context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response
    return HttpResponse("Error while generating PDF")
