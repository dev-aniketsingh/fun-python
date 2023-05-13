import PyPDF4

def copy_pdf_metadata(source_pdf_path, target_pdf_path, output_pdf_path):
    # Open the source and target PDF files
    with open(source_pdf_path, 'rb') as source_file, open(target_pdf_path, 'rb') as target_file:
        # Create PDF reader objects
        source_pdf_reader = PyPDF4.PdfFileReader(source_file)
        target_pdf_reader = PyPDF4.PdfFileReader(target_file)

        # Get metadata from the source PDF file
        metadata = source_pdf_reader.getDocumentInfo()

        # Create a PDF writer object and add the pages from the target PDF
        pdf_writer = PyPDF4.PdfFileWriter()
        for page_num in range(target_pdf_reader.getNumPages()):
            pdf_writer.addPage(target_pdf_reader.getPage(page_num))

        # Update the metadata of the target PDF file
        pdf_writer.addMetadata(metadata)

        # Save the updated target PDF file with the new metadata
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
source_pdf_path = 'pathtosource.pdf'
target_pdf_path = 'targetpdfpath.pdf'
output_pdf_path = 'outputpdf.pdf'
copy_pdf_metadata(source_pdf_path, target_pdf_path, output_pdf_path)


def print_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF4.PdfFileReader(pdf_file)
        metadata = pdf_reader.getDocumentInfo()
        print(f"Metadata for {pdf_path}:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
        print("\n")
        
# Print metadata for the source, target, and output PDF files for confirmation         
print_pdf_metadata(source_pdf_path)
print_pdf_metadata(target_pdf_path)
print_pdf_metadata(output_pdf_path)
