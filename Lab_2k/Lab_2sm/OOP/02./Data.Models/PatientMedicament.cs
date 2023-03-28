using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace P01_HospitalDatabase.Data.Models
{
    [Table("PatientMedicaments")]
    public class PatientMedicament
    {
        //Проміжна таблиця з двома зовнішніми ключами

        [Required]
        [ForeignKey("Medicament")]
        public int MedicamentId { get; set; }
        public Medicament Medicament { get; set; }

        [Required]
        [ForeignKey("Patient")]
        public int PatientId { get; set; }
        public Patient Patient { get; set; }

    }
}