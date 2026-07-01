# Audit journalier AOS - {{date}}

## Resume executif

- Decision d'audit : {{GO / GO partiel / Audit Aion recommande / Blocage}}
- Niveau de risque maximal : {{faible / moyen / eleve / bloquant}}
- Commit audite : {{commit}}
- Periode auditee : {{periode}}
- Rapport genere le : {{datetime}}
- Alertes prioritaires Aion : {{nombre_alertes_prioritaires}}
- Alertes traitees ou attenuees : {{nombre_alertes_traitees_ou_attenuees}}
- Alertes totales detectees : {{nombre_alertes_total}}

## À traiter par Aion

{{a_traiter_par_aion}}

## Alertes traitées ou déjà atténuées

{{alertes_traitees_ou_attenuees}}

## Periode auditee

{{periode_detail}}

## Commits analyses

{{commits_analyses}}

## Classification des commits

### Knowledge batch

{{commits_knowledge_batch}}

### Protocol / system

{{commits_protocol_system}}

### Maintenance

{{commits_maintenance}}

### Audit

{{commits_audit}}

## Commits ignorés pour audit connaissance

{{commits_ignores_audit_connaissance}}

## Fichiers crees

{{fichiers_crees}}

## Fichiers modifies

{{fichiers_modifies}}

## Fiches permanentes impactees

{{fiches_permanentes_impactees}}

## Nouvelles fiches permanentes creees

{{nouvelles_fiches_permanentes}}

## Fiches transversales modifiees

{{fiches_transversales_modifiees}}

## Fiches de veille creees

{{fiches_veille_creees}}

## Sources traitees

{{sources_traitees}}

## Toutes les alertes détectées

{{alertes_detectees}}

## Risques par categorie

### Risque faible

{{risques_faibles}}

### Risque moyen

{{risques_moyens}}

### Risque eleve

{{risques_eleves}}

### Risque bloquant

{{risques_bloquants}}

## Recommandations

{{recommandations}}

## Etat Git final

```text
{{git_status_short}}
```

## Limites de l'audit

- Audit statique et heuristique.
- Ne verifie pas la veracite externe des informations.
- Ne remplace pas la decision qualitative d'Aion.
- Ne corrige aucun contenu automatiquement.
