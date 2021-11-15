<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>FCSC services</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Title</th>
      <th>Annotation</th>
	  <th>Type</th>
	  <th>Version</th>
	  <th>Author</th>
	  <th>Terms</th>
	  <th>Registered</th>
    </tr>
    <xsl:for-each select="services/service">
    <tr>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="annotation"/></td>
      <td><xsl:value-of select="type"/></td>
      <td><xsl:value-of select="version"/></td>
      <td>
       <xsl:for-each select="author">
       <tr>
       <xsl:value-of select="."/>
       </tr>
       </xsl:for-each>
      </td>
      <td><xsl:value-of select="terms"/></td>
      <td><xsl:value-of select="registered"/></td>
    </tr>
    </xsl:for-each>
  </table>	
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 