import React from 'react'

const Table = () => {
  return (
    <table className="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Flat Name</th>
      <th scope="col">Booking ID</th>
      <th scope="col">Check In</th>
      <th scope="col">Check Out</th>
      <th scope="col">Previous Booking ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
  </tbody>
</table>
  )
}

export default Table