using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace iDiTect.Converter.Demo
{
    class Program
    {
        static void Main(string[] args)
        {
            Program converter = new Program();

            //Load rtf document from stream
            using (Stream stream = File.OpenRead("resume.rtf"))
            {
                converter.Load(stream);
            }

            //Convert rtf to pdf, and save it to byte array
            File.WriteAllBytes("convert.pdf", converter.SaveAsBytes());

        }

        
    }
}

