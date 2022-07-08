# Modified VERIS Incident Data: Medical Industry

For this exercise, we have taken [VERIS](https://github.com/vz-risk/veris)-formatted incident data from the VERIS Community Database [VCDB](https://github.com/vz-risk/VCDB) and modified it to be more quickly understood and explored for the purposes of this exercise.

VERIS, the Vocabulary for Event Recording and Incident Sharing, is a common language for describing security incidents in a structured manner. It was invented and is maintained by the Verizon RISK team, and the most current documentation for the entire schema may be [found on GitHub](https://github.com/vz-risk/veris) and at [veriscommunity.net](http://veriscommunity.net/). The VCDB is an open-source data set in VERIS format, also maintained by the Verizon RISK team and several community contributors. The data set is licensed with the Creative Commons Attribution-ShareAlike 4.0 International Public License. Please see the [VCDB License file](https://github.com/vz-risk/VCDB/blob/master/LICENSE.txt) for more information. 

## How we Modified the Data

As of the writing of this document, the VCDB consists of 8192 incidents, and when parsed with the [verispy](https://github.com/RiskLens/verispy) Python package, has 2330 features (columns). 

Because this would be extremely unwieldy for a take-home exercise with a target time of 4-5 hours, we have simplified the data set by doing the following:  

  * Limiting the data set to incidents in the medical industry (NAICS 2-digit code: 62).  
  * Compacting some enumerations and wholly eliminating many of them. Unfortunately, this does cause a problem when, for instance, there is more than one actor or one action involved in an incident. So, user beware: your findings may be interesting and applicable in context of what you are asked to do for this exercise, but you should use the full VCDB data set if you wish to make grand pronouncements about the state of cybersecurity breaches.  

 This leaves us with a current data set of 2252 rows and 22 columns as of this writing, which should be more tractable for this exercise.  

 For documentation and code showing how the data set was built, please see the [Build_Data_Set](Build_Data_Set.ipynb) Jupyter Notebook in this repository (not required).  

 # Variable Descriptions (Code Book) 

 A listing of all the features -- their names and descriptions -- for our modified data set is shown below. Links to additional information are included for the curious, but is not necessary to complete this exercise. 

   * **incident_id**: Incident or case ID. Corresponds to the JSON filename in the [VCDB json directory](https://github.com/vz-risk/VCDB/tree/master/data/json/validated). 
   * **timeline.incident.day**:  Day of month incident occurred.  
   * **timeline.incident.month**: Month incident occurred.  
   * **timeline.incident.time**: Time incident occurred.  
   * **timeline.incident.year**: Year incident occurred.  
   * **actor**: Entities that cause or contribute to an incident. [source](http://veriscommunity.net/actors.html) 
   * **action**: Describe what the threat actor did to cause or contribute to the incident. [source](http://veriscommunity.net/actions.html) 
   * **attribute.confidentiality**: Was this a [confidentiality](https://resources.infosecinstitute.com/cia-triad/) breach (T/F)? [source](http://veriscommunity.net/attributes.html#section-confidentiality) 
   * **attribute.integrity**: Was this an [integrity](https://resources.infosecinstitute.com/cia-triad/) incident (T/F)? [source](http://veriscommunity.net/attributes.html#section-integrity)
   * **attribute.availability**: Was this an [availability](https://resources.infosecinstitute.com/cia-triad/) incident (T/F)? [source](http://veriscommunity.net/attributes.html#section-availability)
   * **asset**: The information assets that were compromised during the incident. [source](http://veriscommunity.net/assets.html) 
   * **asset.variety**: The variety of the asset that was compromised during the event. Prepended with a single-letter abbreviation of the asset class
   * **confidentiality.medical_records**: Count of the number of medical records breached.  
   * **confidentiality.payment_records**: Count of the number of payment records breached.  
   * **confidentiality.personal_records**: Count of the number of personal records breached.  
   * **confidentiality.total_record_count**: Count of the total records breached (includes other classes besides the previous three).  
   * **victim.employee_count**: Number of employees for the victim organization. Small: 1,000 employees or less. Large: 1,001 employees or more. [source](http://veriscommunity.net/enums.html#section-victims)
   * **victim.state**: Victim organization's state (if country == US) 
   * **victim.country**: Victim organization's country, 2-letter code.  See [code_to_country.json](https://github.com/vz-risk/veris/blob/master/code_to_country.json) for the list of country codes (not required for this exercise).  
   * **victim.victim_id**: Name of the victim organization.  
   * **summary**:  Free text summary entered by the user who entered event into VCDB.  
   * **reference**: Usually a link to a news source for the breach.  

Notes:  

  * An event may have one or more attributes (i.e. it could be a confidentiality breach and an integrity incident at the same time). 
  * Events often have more than one actor, action, or asset affected. In order to keep the data relatively simplified, in these cases we chose just a single entry for these features for each incident.  
  * The `attribute` features are part of the [CIA triad](https://whatis.techtarget.com/definition/Confidentiality-integrity-and-availability-CIA). 
