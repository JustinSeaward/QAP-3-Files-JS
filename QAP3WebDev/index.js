// Desc: Program for Mos lawn care services.
// Author: Justin Seaward.
// Dates: July 16, 2025 - July 19, 2025.


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const BORDER_AREA_ESP = .04; // 4% of the total square footage of boarder.
const BORDER_COST = .35;     // 0.35 cent charge per square foot.

const LAWN_AREA_ESP = .95;   // 95% of the total square footage of lawn.
const LAWN_MOW_COST = .07;   // 0.07 cent charge per square foot.
const FERT_COST = .05;       // 0.05 cent charge per square foot.

const HST_ESP = .15;         // 15% tax rate for the HST.
const ENVIRO_ESP = .0014;    // 3% charge for the environmental tax.


// Start main program here. //

// Gather user input. //

// Input customer full name.
let custName = prompt("Enter the customer name: ");

// Input customer street address.
let stAdd = prompt("Enter the customer street adresses: ");

// Input customer city.
let city = prompt("Enter the customer city: ");

// Input customer phone number.
let phoNum = prompt("Enter the customers phone number: ");
let phoNumDsp = phoNum.slice(0,3) + "-" + phoNum.slice(4,6) + "-" + phoNum.slice(6,11);

// Input total square footage of the customers lawn.
let totSqFt = prompt("Enter the total square footage: ");
totSqFt = parseInt(totSqFt);

// Calculations for program. //

// Calculation for border size and cost.
let bordSize = totSqFt * BORDER_AREA_ESP;
let bordCost = bordSize * BORDER_COST;

// Calculation for lawn size and cost.
let lawnSize = totSqFt * LAWN_AREA_ESP;
let lawnCost = lawnSize * LAWN_MOW_COST;

// Calculation for fertilizer treatment cost.
let fertCost = totSqFt * FERT_COST;

// Calculation for total charges.
let totalCharge = bordCost + lawnCost + fertCost;

// Calculation for sales tax.
let hST = totalCharge * HST_ESP;

// Calculation for enrivomental tax.
let envirTax = totalCharge * ENVIRO_ESP;

// Calculation for invoice total.
let invTot = totalCharge + hST + envirTax;

// Display customer receipt in a table.

document.writeln("<br />");
document.writeln("<table class='lawntable'>");

document.writeln("<tr class='tophead'>");
document.writeln("<td colspan='2'>Mo's Lawncare Services - Customer Invoice</td>")
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2'>");
document.writeln("<br />&nbsp; Customer details:<br /><br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + custName + "<br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + stAdd + "<br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + city + "," + "&nbsp;" + phoNumDsp + "<br />");
document.writeln("<br />")
document.writeln("&nbsp;&nbsp;Property size (in Sq Ft): &nbsp;" + totSqFt + "<br />");
document.writeln("<br />");
document.writeln("</td>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Border cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(bordCost) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Mowing cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(lawnCost) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Fertilizer cost: <br /></td>");
document.writeln("<td class='righttext'>" + cur2Format.format(fertCost) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td>" + "<br/>" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Total charges:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(totalCharge) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td>" + "<br/>" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Sales tax (HST): </td>");
document.writeln("<td class='righttext'>" + cur2Format.format(hST) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Environmental tax: </td>");
document.writeln("<td class='righttext'>" + cur2Format.format(envirTax) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'>" + "<br/>" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>&nbsp; Invoice total: </td>");
document.writeln("<td class='righttext'>" + cur2Format.format(invTot) + "&nbsp;" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='bottomfoot'>Turning Lawns into Landscapes</td>");
document.writeln("</tr>");

document.writeln("</table>");