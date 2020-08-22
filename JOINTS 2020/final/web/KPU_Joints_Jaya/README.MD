# Pemilu Joints Jaya 2019

### Description
Pemilu tahun 2019 sudah terlewati, namun pada bulan ini, terdapat sebuah 
kasus data breach sejumlah 200 juta data yang menimpa KPU Joints Jaya.
Mohon bantu kami mencari celahnya agar bisa kami perbaiki.

### Bug Desc
Ada dua vuln
- Spring boot Path Transversal
- Spring boot actuator versi lama yang ada endpoint /heapdump
Jadi intinya kan pas awal admin-daemon bakal melakukan post request untuk daftar
admin baru, nah itu nanti data requestnya bakal disimpen di memory, heapdump ini
nanti bisa ngedump semua data yang ada di memorynya.

## Credit
- cacadosman
- naifriot