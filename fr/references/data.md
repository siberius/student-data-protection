# 4. Modèle de données, collecte et minimisation [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 4.

## 4. Modèle de données, collecte et minimisation [P]

[P] Le modèle de données de l'application DOIT respecter le principe de minimisation:
- **Identifiants:** Utiliser des UUIDv4 synthétiques comme clés primaires. Ne jamais exposer le numéro d'identification national (INE en France) ni le nom de l'élève dans les URL ou le stockage local.
- **Champs facultatifs:** Les numéros de téléphone personnel, adresses postales et photographies ne doivent pas être obligatoires dans les applications disciplinaires.
- **Données sensibles:** Les applications pédagogiques NE DOIVENT PAS collecter de diagnostics médicaux. Pour les aménagements d'épreuves (tiers-temps), seul un paramètre technique (`extra_time_multiplier: 1.33`) doit être conservé.
- **Métadonnées:** Purger systématiquement les métadonnées EXIF des photos de devoirs téléversées par les élèves avant stockage.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
