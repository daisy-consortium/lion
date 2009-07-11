<?xml version="1.0" encoding="UTF-8"?>

<!-- Create the XHTML project import to record prompts in Obi. Uses the
  - -strings input format from managedb. -->

<xsl:transform version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="xml" version="1.0" encoding="UTF-8"
    omit-xml-declaration="no" indent="yes"
    doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>

  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <title>
          <xsl:value-of select="concat('Prompts for ',strings/@langid)"/>
        </title>
      </head>
      <body>
        <xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="s">
    <h1 xmlns="http://www.w3.org/1999/xhtml" id="{@id}">
      <xsl:value-of select="."/>
    </h1>
  </xsl:template>

</xsl:transform>
