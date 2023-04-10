using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace StudentSystem.Migrations
{
    public partial class SeedData : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 1,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 53, 20, 503, DateTimeKind.Local).AddTicks(9862));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 2,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 53, 20, 503, DateTimeKind.Local).AddTicks(9862));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 3,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 53, 20, 503, DateTimeKind.Local).AddTicks(9862));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 4,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 53, 20, 501, DateTimeKind.Local).AddTicks(9851));
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 1,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 32, 35, 534, DateTimeKind.Local).AddTicks(6920));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 2,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 32, 35, 534, DateTimeKind.Local).AddTicks(6920));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 3,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 32, 35, 534, DateTimeKind.Local).AddTicks(6920));

            migrationBuilder.UpdateData(
                table: "Students",
                keyColumn: "StudentId",
                keyValue: 4,
                column: "RegisteredOn",
                value: new DateTime(2023, 4, 9, 23, 32, 35, 532, DateTimeKind.Local).AddTicks(6919));
        }
    }
}
