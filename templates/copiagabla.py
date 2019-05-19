 <center>  
      <table border = 2>
         <thead>
            <td align="center"><strong>Servicio</strong></td>
            <td align="center"> <strong>Descripción</strong></td>
            <td align="center"><strong>Disponibilidad</strong></td>
            <td align="center"><strong>Precio/hora</strong></td>
            <td align="center"><strong>Teléfono</strong></td>
            <td align="center"><strong>Correo </strong></td>
         </thead>
         
         {% for row in rows %}
            <tr>
               <td align="center">{{row["Servicio"]}}</td>
               <td align="center">{{row["Descripcion_del_producto"]}}</td>
               <td align="center">{{row["Horas_por_semana"]}}</td>
               <td align="center"> {{ row["Precio_por_hora"]}}</td>
               <td align="center">{{row['Contacto']}}</td>	
               <td align="center"> {{ row["Correo"]}}</td>
            </tr>
         {% endfor %}
      </table>
        </center> 
