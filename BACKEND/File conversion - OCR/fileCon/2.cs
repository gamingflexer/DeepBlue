// Load the RTF file to be converted
var document = new Aspose.Words.Document("resume.rtf");
// Convert RTF to a PDF
document.Save("Document.pdf", Aspose.Words.SaveFormat.Pdf); 