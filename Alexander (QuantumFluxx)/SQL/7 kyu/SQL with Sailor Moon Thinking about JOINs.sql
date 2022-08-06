SELECT senshi_name AS sailor_senshi, real_name_jpn AS real_name, 
       cats.name AS cat, schools.school AS school
FROM sailorsenshi 
LEFT JOIN schools 
ON sailorsenshi.school_id=schools.id
LEFT JOIN cats
ON sailorsenshi.cat_id=c